[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/test/TestCase)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/test/TestCase?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Ftest%2FTestCase&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#child_classes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#methods)
    *   [addClassCleanup](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#addClassCleanup)
        
    *   [addCleanup](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#addCleanup)
        
    *   [addTypeEqualityFunc](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#addTypeEqualityFunc)
        
    *   [assertAllClose](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertAllClose)
        
    *   [assertAllCloseAccordingToType](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertAllCloseAccordingToType)
        
    *   [assertAllEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertAllEqual)
        
    *   [assertAllGreater](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertAllGreater)
        
    *   [assertAllGreaterEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertAllGreaterEqual)
        
    *   [assertAllInRange](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertAllInRange)
        
    *   [assertAllInSet](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertAllInSet)
        
    *   [assertAllLess](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertAllLess)
        
    *   [assertAllLessEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertAllLessEqual)
        
    *   [assertAlmostEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertAlmostEqual)
        
    *   [assertAlmostEquals](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertAlmostEquals)
        
    *   [assertArrayNear](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertArrayNear)
        
    *   [assertBetween](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertBetween)
        
    *   [assertCommandFails](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertCommandFails)
        
    *   [assertCommandSucceeds](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertCommandSucceeds)
        
    *   [assertContainsExactSubsequence](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertContainsExactSubsequence)
        
    *   [assertContainsInOrder](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertContainsInOrder)
        
    *   [assertContainsSubsequence](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertContainsSubsequence)
        
    *   [assertContainsSubset](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertContainsSubset)
        
    *   [assertCountEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertCountEqual)
        
    *   [assertDTypeEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertDTypeEqual)
        
    *   [assertDataclassEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertDataclassEqual)
        
    *   [assertDeviceEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertDeviceEqual)
        
    *   [assertDictAlmostEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertDictAlmostEqual)
        
    *   [assertDictContainsSubset](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertDictContainsSubset)
        
    *   [assertDictEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertDictEqual)
        
    *   [assertEmpty](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertEmpty)
        
    *   [assertEndsWith](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertEndsWith)
        
    *   [assertEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertEqual)
        
    *   [assertEquals](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertEquals)
        
    *   [assertFalse](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertFalse)
        
    *   [assertGreater](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertGreater)
        
    *   [assertGreaterEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertGreaterEqual)
        
    *   [assertIn](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertIn)
        
    *   [assertIs](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertIs)
        
    *   [assertIsInstance](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertIsInstance)
        
    *   [assertIsNone](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertIsNone)
        
    *   [assertIsNot](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertIsNot)
        
    *   [assertIsNotNone](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertIsNotNone)
        
    *   [assertIsSubclass](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertIsSubclass)
        
    *   [assertItemsEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertItemsEqual)
        
    *   [assertJsonEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertJsonEqual)
        
    *   [assertLen](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertLen)
        
    *   [assertLess](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertLess)
        
    *   [assertLessEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertLessEqual)
        
    *   [assertListEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertListEqual)
        
    *   [assertLogs](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertLogs)
        
    *   [assertMappingEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertMappingEqual)
        
    *   [assertMultiLineEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertMultiLineEqual)
        
    *   [assertNDArrayNear](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNDArrayNear)
        
    *   [assertNear](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNear)
        
    *   [assertNoCommonElements](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNoCommonElements)
        
    *   [assertNoLogs](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNoLogs)
        
    *   [assertNotAllClose](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNotAllClose)
        
    *   [assertNotAllEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNotAllEqual)
        
    *   [assertNotAlmostEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNotAlmostEqual)
        
    *   [assertNotAlmostEquals](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNotAlmostEquals)
        
    *   [assertNotEmpty](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNotEmpty)
        
    *   [assertNotEndsWith](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNotEndsWith)
        
    *   [assertNotEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNotEqual)
        
    *   [assertNotEquals](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNotEquals)
        
    *   [assertNotIn](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNotIn)
        
    *   [assertNotIsInstance](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNotIsInstance)
        
    *   [assertNotIsSubclass](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNotIsSubclass)
        
    *   [assertNotRegex](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNotRegex)
        
    *   [assertNotRegexpMatches](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNotRegexpMatches)
        
    *   [assertNotStartsWith](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNotStartsWith)
        
    *   [assertProtoEquals](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertProtoEquals)
        
    *   [assertProtoEqualsVersion](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertProtoEqualsVersion)
        
    *   [assertRaises](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertRaises)
        
    *   [assertRaisesIncompatibleShapesError](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertRaisesIncompatibleShapesError)
        
    *   [assertRaisesOpError](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertRaisesOpError)
        
    *   [assertRaisesRegex](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertRaisesRegex)
        
    *   [assertRaisesRegexp](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertRaisesRegexp)
        
    *   [assertRaisesWithLiteralMatch](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertRaisesWithLiteralMatch)
        
    *   [assertRaisesWithPredicateMatch](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertRaisesWithPredicateMatch)
        
    *   [assertRegex](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertRegex)
        
    *   [assertRegexMatch](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertRegexMatch)
        
    *   [assertRegexpMatches](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertRegexpMatches)
        
    *   [assertSameElements](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertSameElements)
        
    *   [assertSameStructure](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertSameStructure)
        
    *   [assertSequenceAlmostEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertSequenceAlmostEqual)
        
    *   [assertSequenceEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertSequenceEqual)
        
    *   [assertSequenceStartsWith](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertSequenceStartsWith)
        
    *   [assertSetEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertSetEqual)
        
    *   [assertShapeEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertShapeEqual)
        
    *   [assertStartsWith](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertStartsWith)
        
    *   [assertTotallyOrdered](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertTotallyOrdered)
        
    *   [assertTrue](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertTrue)
        
    *   [assertTupleEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertTupleEqual)
        
    *   [assertUrlEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertUrlEqual)
        
    *   [assertWarns](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertWarns)
        
    *   [assertWarnsRegex](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertWarnsRegex)
        
    *   [assert\_](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assert_)
        
    *   [cached\_session](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#cached_session)
        
    *   [captureWritesToStream](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#captureWritesToStream)
        
    *   [checkedThread](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#checkedThread)
        
    *   [countTestCases](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#countTestCases)
        
    *   [create\_tempdir](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#create_tempdir)
        
    *   [create\_tempfile](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#create_tempfile)
        
    *   [debug](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#debug)
        
    *   [defaultTestResult](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#defaultTestResult)
        
    *   [doClassCleanups](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#doClassCleanups)
        
    *   [doCleanups](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#doCleanups)
        
    *   [enterClassContext](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#enterClassContext)
        
    *   [enterContext](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#enterContext)
        
    *   [enter\_context](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#enter_context)
        
    *   [evaluate](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#evaluate)
        
    *   [evaluate\_if\_both\_tensors](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#evaluate_if_both_tensors)
        
    *   [fail](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#fail)
        
    *   [failIf](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#failIf)
        
    *   [failIfAlmostEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#failIfAlmostEqual)
        
    *   [failIfEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#failIfEqual)
        
    *   [failUnless](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#failUnless)
        
    *   [failUnlessAlmostEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#failUnlessAlmostEqual)
        
    *   [failUnlessEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#failUnlessEqual)
        
    *   [failUnlessRaises](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#failUnlessRaises)
        
    *   [get\_recorded\_properties](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#get_recorded_properties)
        
    *   [get\_temp\_dir](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#get_temp_dir)
        
    *   [id](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#id)
        
    *   [record\_property](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#record_property)
        
    *   [run](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#run)
        
    *   [session](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#session)
        
    *   [setUp](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#setUp)
        
    *   [setUpClass](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#setUpClass)
        
    *   [shortDescription](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#shortDescription)
        
    *   [skipTest](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#skipTest)
        
    *   [subTest](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#subTest)
        
    *   [tearDown](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#tearDown)
        
    *   [tearDownClass](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#tearDownClass)
        
    *   [test\_session](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#test_session)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#__call__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.test.TestCase Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#child_classes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#methods)
    *   [addClassCleanup](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#addClassCleanup)
        
    *   [addCleanup](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#addCleanup)
        
    *   [addTypeEqualityFunc](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#addTypeEqualityFunc)
        
    *   [assertAllClose](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertAllClose)
        
    *   [assertAllCloseAccordingToType](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertAllCloseAccordingToType)
        
    *   [assertAllEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertAllEqual)
        
    *   [assertAllGreater](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertAllGreater)
        
    *   [assertAllGreaterEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertAllGreaterEqual)
        
    *   [assertAllInRange](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertAllInRange)
        
    *   [assertAllInSet](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertAllInSet)
        
    *   [assertAllLess](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertAllLess)
        
    *   [assertAllLessEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertAllLessEqual)
        
    *   [assertAlmostEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertAlmostEqual)
        
    *   [assertAlmostEquals](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertAlmostEquals)
        
    *   [assertArrayNear](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertArrayNear)
        
    *   [assertBetween](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertBetween)
        
    *   [assertCommandFails](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertCommandFails)
        
    *   [assertCommandSucceeds](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertCommandSucceeds)
        
    *   [assertContainsExactSubsequence](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertContainsExactSubsequence)
        
    *   [assertContainsInOrder](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertContainsInOrder)
        
    *   [assertContainsSubsequence](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertContainsSubsequence)
        
    *   [assertContainsSubset](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertContainsSubset)
        
    *   [assertCountEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertCountEqual)
        
    *   [assertDTypeEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertDTypeEqual)
        
    *   [assertDataclassEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertDataclassEqual)
        
    *   [assertDeviceEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertDeviceEqual)
        
    *   [assertDictAlmostEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertDictAlmostEqual)
        
    *   [assertDictContainsSubset](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertDictContainsSubset)
        
    *   [assertDictEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertDictEqual)
        
    *   [assertEmpty](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertEmpty)
        
    *   [assertEndsWith](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertEndsWith)
        
    *   [assertEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertEqual)
        
    *   [assertEquals](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertEquals)
        
    *   [assertFalse](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertFalse)
        
    *   [assertGreater](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertGreater)
        
    *   [assertGreaterEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertGreaterEqual)
        
    *   [assertIn](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertIn)
        
    *   [assertIs](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertIs)
        
    *   [assertIsInstance](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertIsInstance)
        
    *   [assertIsNone](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertIsNone)
        
    *   [assertIsNot](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertIsNot)
        
    *   [assertIsNotNone](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertIsNotNone)
        
    *   [assertIsSubclass](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertIsSubclass)
        
    *   [assertItemsEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertItemsEqual)
        
    *   [assertJsonEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertJsonEqual)
        
    *   [assertLen](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertLen)
        
    *   [assertLess](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertLess)
        
    *   [assertLessEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertLessEqual)
        
    *   [assertListEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertListEqual)
        
    *   [assertLogs](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertLogs)
        
    *   [assertMappingEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertMappingEqual)
        
    *   [assertMultiLineEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertMultiLineEqual)
        
    *   [assertNDArrayNear](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNDArrayNear)
        
    *   [assertNear](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNear)
        
    *   [assertNoCommonElements](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNoCommonElements)
        
    *   [assertNoLogs](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNoLogs)
        
    *   [assertNotAllClose](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNotAllClose)
        
    *   [assertNotAllEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNotAllEqual)
        
    *   [assertNotAlmostEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNotAlmostEqual)
        
    *   [assertNotAlmostEquals](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNotAlmostEquals)
        
    *   [assertNotEmpty](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNotEmpty)
        
    *   [assertNotEndsWith](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNotEndsWith)
        
    *   [assertNotEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNotEqual)
        
    *   [assertNotEquals](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNotEquals)
        
    *   [assertNotIn](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNotIn)
        
    *   [assertNotIsInstance](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNotIsInstance)
        
    *   [assertNotIsSubclass](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNotIsSubclass)
        
    *   [assertNotRegex](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNotRegex)
        
    *   [assertNotRegexpMatches](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNotRegexpMatches)
        
    *   [assertNotStartsWith](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertNotStartsWith)
        
    *   [assertProtoEquals](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertProtoEquals)
        
    *   [assertProtoEqualsVersion](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertProtoEqualsVersion)
        
    *   [assertRaises](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertRaises)
        
    *   [assertRaisesIncompatibleShapesError](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertRaisesIncompatibleShapesError)
        
    *   [assertRaisesOpError](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertRaisesOpError)
        
    *   [assertRaisesRegex](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertRaisesRegex)
        
    *   [assertRaisesRegexp](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertRaisesRegexp)
        
    *   [assertRaisesWithLiteralMatch](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertRaisesWithLiteralMatch)
        
    *   [assertRaisesWithPredicateMatch](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertRaisesWithPredicateMatch)
        
    *   [assertRegex](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertRegex)
        
    *   [assertRegexMatch](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertRegexMatch)
        
    *   [assertRegexpMatches](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertRegexpMatches)
        
    *   [assertSameElements](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertSameElements)
        
    *   [assertSameStructure](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertSameStructure)
        
    *   [assertSequenceAlmostEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertSequenceAlmostEqual)
        
    *   [assertSequenceEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertSequenceEqual)
        
    *   [assertSequenceStartsWith](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertSequenceStartsWith)
        
    *   [assertSetEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertSetEqual)
        
    *   [assertShapeEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertShapeEqual)
        
    *   [assertStartsWith](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertStartsWith)
        
    *   [assertTotallyOrdered](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertTotallyOrdered)
        
    *   [assertTrue](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertTrue)
        
    *   [assertTupleEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertTupleEqual)
        
    *   [assertUrlEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertUrlEqual)
        
    *   [assertWarns](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertWarns)
        
    *   [assertWarnsRegex](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assertWarnsRegex)
        
    *   [assert\_](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#assert_)
        
    *   [cached\_session](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#cached_session)
        
    *   [captureWritesToStream](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#captureWritesToStream)
        
    *   [checkedThread](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#checkedThread)
        
    *   [countTestCases](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#countTestCases)
        
    *   [create\_tempdir](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#create_tempdir)
        
    *   [create\_tempfile](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#create_tempfile)
        
    *   [debug](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#debug)
        
    *   [defaultTestResult](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#defaultTestResult)
        
    *   [doClassCleanups](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#doClassCleanups)
        
    *   [doCleanups](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#doCleanups)
        
    *   [enterClassContext](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#enterClassContext)
        
    *   [enterContext](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#enterContext)
        
    *   [enter\_context](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#enter_context)
        
    *   [evaluate](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#evaluate)
        
    *   [evaluate\_if\_both\_tensors](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#evaluate_if_both_tensors)
        
    *   [fail](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#fail)
        
    *   [failIf](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#failIf)
        
    *   [failIfAlmostEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#failIfAlmostEqual)
        
    *   [failIfEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#failIfEqual)
        
    *   [failUnless](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#failUnless)
        
    *   [failUnlessAlmostEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#failUnlessAlmostEqual)
        
    *   [failUnlessEqual](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#failUnlessEqual)
        
    *   [failUnlessRaises](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#failUnlessRaises)
        
    *   [get\_recorded\_properties](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#get_recorded_properties)
        
    *   [get\_temp\_dir](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#get_temp_dir)
        
    *   [id](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#id)
        
    *   [record\_property](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#record_property)
        
    *   [run](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#run)
        
    *   [session](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#session)
        
    *   [setUp](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#setUp)
        
    *   [setUpClass](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#setUpClass)
        
    *   [shortDescription](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#shortDescription)
        
    *   [skipTest](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#skipTest)
        
    *   [subTest](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#subTest)
        
    *   [tearDown](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#tearDown)
        
    *   [tearDownClass](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#tearDownClass)
        
    *   [test\_session](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#test_session)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#__call__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/test/TestCase#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L2564-L4003)

Base class for tests that need to test TensorFlow.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.test.TestCase`](https://www.tensorflow.org/api_docs/python/tf/test/TestCase)

tf.test.TestCase(
        methodName='runTest'
    )

Child Classes
-------------

[`class failureException`](https://www.tensorflow.org/api_docs/python/tf/test/TestCase/failureException)

Methods
-------

### `addClassCleanup`

@classmethod

Same as addCleanup, except the cleanup items are called even if setUpClass fails (unlike tearDownClass).

### `addCleanup`

addCleanup(
        function, *args, /, **kwargs
    )

Add a function, with arguments, to be called when the test is completed. Functions added are called on a LIFO basis and are called after tearDown on test failure or success.

Cleanup items are called even if setUp fails (unlike tearDown).

### `addTypeEqualityFunc`

addTypeEqualityFunc(
        typeobj, function
    )

Add a type specific assertEqual style function to compare a type.

This method is for use by TestCase subclasses that need to register their own type equality functions to provide nicer error messages.

|     |     |
| --- | --- |
| Args |     |
| `typeobj` | The data type to call this function on when both values are of the same type in assertEqual(). |
| `function` | The callable taking two arguments and an optional msg= argument that raises self.failureException with a useful error message when the two arguments are not equal. |

### `assertAllClose`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L3352-L3383)

assertAllClose(
        a, b, rtol=1e-06, atol=1e-06, msg=None
    )

Asserts that two structures of numpy arrays or Tensors, have near values.

`a` and `b` can be arbitrarily nested structures. A layer of a nested structure can be a `dict`, `namedtuple`, `tuple` or `list`.

|     |     |
| --- | --- |
| Args |     |
| `a` | The expected numpy `ndarray`, or anything that can be converted into a numpy `ndarray` (including Tensor), or any arbitrarily nested of structure of these. |
| `b` | The actual numpy `ndarray`, or anything that can be converted into a numpy `ndarray` (including Tensor), or any arbitrarily nested of structure of these. |
| `rtol` | relative tolerance. |
| `atol` | absolute tolerance. |
| `msg` | Optional message to report on failure. |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | if only one of `a[p]` and `b[p]` is a dict or `a[p]` and `b[p]` have different length, where `[p]` denotes a path to the nested structure, e.g. given `a = [(1, 1), {'d': (6, 7)}]` and `[p] = [1]['d']`, then `a[p] = (6, 7)`. |

### `assertAllCloseAccordingToType`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L3385-L3432)

assertAllCloseAccordingToType(
        a,
        b,
        rtol=1e-06,
        atol=1e-06,
        float_rtol=1e-06,
        float_atol=1e-06,
        half_rtol=0.001,
        half_atol=0.001,
        bfloat16_rtol=0.01,
        bfloat16_atol=0.01,
        msg=None
    )

Like assertAllClose, but also suitable for comparing fp16 arrays.

In particular, the tolerance is reduced to 1e-3 if at least one of the arguments is of type float16.

|     |     |
| --- | --- |
| Args |     |
| `a` | the expected numpy ndarray or anything can be converted to one. |
| `b` | the actual numpy ndarray or anything can be converted to one. |
| `rtol` | relative tolerance. |
| `atol` | absolute tolerance. |
| `float_rtol` | relative tolerance for float32. |
| `float_atol` | absolute tolerance for float32. |
| `half_rtol` | relative tolerance for float16. |
| `half_atol` | absolute tolerance for float16. |
| `bfloat16_rtol` | relative tolerance for bfloat16. |
| `bfloat16_atol` | absolute tolerance for bfloat16. |
| `msg` | Optional message to report on failure. |

### `assertAllEqual`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L3459-L3517)

assertAllEqual(
        a, b, msg=None
    )

Asserts that two numpy arrays or Tensors have the same values.

|     |     |
| --- | --- |
| Args |     |
| `a` | the expected numpy ndarray or anything can be converted to one. |
| `b` | the actual numpy ndarray or anything can be converted to one. |
| `msg` | Optional message to report on failure. |

### `assertAllGreater`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L3535-L3546)

assertAllGreater(
        a, comparison_target
    )

Assert element values are all greater than a target value.

|     |     |
| --- | --- |
| Args |     |
| `a` | The numpy `ndarray`, or anything that can be converted into a numpy `ndarray` (including Tensor). |
| `comparison_target` | The target value of comparison. |

### `assertAllGreaterEqual`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L3561-L3572)

assertAllGreaterEqual(
        a, comparison_target
    )

Assert element values are all greater than or equal to a target value.

|     |     |
| --- | --- |
| Args |     |
| `a` | The numpy `ndarray`, or anything that can be converted into a numpy `ndarray` (including Tensor). |
| `comparison_target` | The target value of comparison. |

### `assertAllInRange`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L3620-L3677)

assertAllInRange(
        target,
        lower_bound,
        upper_bound,
        open_lower_bound=False,
        open_upper_bound=False
    )

Assert that elements in a Tensor are all in a given range.

|     |     |
| --- | --- |
| Args |     |
| `target` | The numpy `ndarray`, or anything that can be converted into a numpy `ndarray` (including Tensor). |
| `lower_bound` | lower bound of the range |
| `upper_bound` | upper bound of the range |
| `open_lower_bound` | (`bool`) whether the lower bound is open (i.e., > rather than the default >=) |
| `open_upper_bound` | (`bool`) whether the upper bound is open (i.e., < rather than the default <=) |

|     |     |
| --- | --- |
| Raises |     |
| `AssertionError` | if the value tensor does not have an ordered numeric type (float\* or int\*), or if there are nan values, or if any of the elements do not fall in the specified range. |

### `assertAllInSet`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L3679-L3699)

assertAllInSet(
        target, expected_set
    )

Assert that elements of a Tensor are all in a given closed set.

|     |     |
| --- | --- |
| Args |     |
| `target` | The numpy `ndarray`, or anything that can be converted into a numpy `ndarray` (including Tensor). |
| `expected_set` | (`list`, `tuple` or `set`) The closed set that the elements of the value of `target` are expected to fall into. |

|     |     |
| --- | --- |
| Raises |     |
| `AssertionError` | if any of the elements do not fall into `expected_set`. |

### `assertAllLess`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L3548-L3559)

assertAllLess(
        a, comparison_target
    )

Assert element values are all less than a target value.

|     |     |
| --- | --- |
| Args |     |
| `a` | The numpy `ndarray`, or anything that can be converted into a numpy `ndarray` (including Tensor). |
| `comparison_target` | The target value of comparison. |

### `assertAllLessEqual`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L3574-L3585)

assertAllLessEqual(
        a, comparison_target
    )

Assert element values are all less than or equal to a target value.

|     |     |
| --- | --- |
| Args |     |
| `a` | The numpy `ndarray`, or anything that can be converted into a numpy `ndarray` (including Tensor). |
| `comparison_target` | The target value of comparison. |

### `assertAlmostEqual`

assertAlmostEqual(
        first, second, places=None, msg=None, delta=None
    )

Fail if the two objects are unequal as determined by their difference rounded to the given number of decimal places (default 7) and comparing to zero, or by comparing that the difference between the two objects is more than the given delta.

Note that decimal places (from zero) are usually not the same as significant digits (measured from the most significant digit).

If the two objects compare equal then they will automatically compare almost equal.

### `assertAlmostEquals`

assertAlmostEquals(
        *args, **kwargs
    )

### `assertArrayNear`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L3155-L3170)

assertArrayNear(
        farray1, farray2, err, msg=None
    )

Asserts that two float arrays are near each other.

Checks that for all elements of farray1 and farray2 |f1 - f2| < err. Asserts a test failure if not.

|     |     |
| --- | --- |
| Args |     |
| `farray1` | a list of float values. |
| `farray2` | a list of float values. |
| `err` | a float value. |
| `msg` | Optional message to report on failure. |

### `assertBetween`

assertBetween(
        value, minv, maxv, msg=None
    )

Asserts that value is between minv and maxv (inclusive).

### `assertCommandFails`

assertCommandFails(
        command, regexes, env=None, close_fds=True, msg=None
    )

Asserts a shell command fails and the error matches a regex in a list.

|     |     |
| --- | --- |
| Args |     |
| `command` | List or string representing the command to run. |
| `regexes` | the list of regular expression strings. |
| `env` | Dictionary of environment variable settings. If None, no environment variables will be set for the child process. This is to make tests more hermetic. NOTE: this behavior is different than the standard subprocess module. |
| `close_fds` | Whether or not to close all open fd's in the child after forking. |
| `msg` | Optional message to report on failure. |

### `assertCommandSucceeds`

assertCommandSucceeds(
        command, regexes=(b'',), env=None, close_fds=True, msg=None
    )

Asserts that a shell command succeeds (i.e. exits with code 0).

|     |     |
| --- | --- |
| Args |     |
| `command` | List or string representing the command to run. |
| `regexes` | List of regular expression byte strings that match success. |
| `env` | Dictionary of environment variable settings. If None, no environment variables will be set for the child process. This is to make tests more hermetic. NOTE: this behavior is different than the standard subprocess module. |
| `close_fds` | Whether or not to close all open fd's in the child after forking. |
| `msg` | Optional message to report on failure. |

### `assertContainsExactSubsequence`

assertContainsExactSubsequence(
        container, subsequence, msg=None
    )

Asserts that "container" contains "subsequence" as an exact subsequence.

Asserts that "container" contains all the elements of "subsequence", in order, and without other elements interspersed. For example, \[1, 2, 3\] is an exact subsequence of \[0, 0, 1, 2, 3, 0\] but not of \[0, 0, 1, 2, 0, 3, 0\].

|     |     |
| --- | --- |
| Args |     |
| `container` | the list we're testing for subsequence inclusion. |
| `subsequence` | the list we hope will be an exact subsequence of container. |
| `msg` | Optional message to report on failure. |

### `assertContainsInOrder`

assertContainsInOrder(
        strings, target, msg=None
    )

Asserts that the strings provided are found in the target in order.

This may be useful for checking HTML output.

|     |     |
| --- | --- |
| Args |     |
| `strings` | A list of strings, such as \[ 'fox', 'dog' \] |
| `target` | A target string in which to look for the strings, such as 'The quick brown fox jumped over the lazy dog'. |
| `msg` | Optional message to report on failure. |

### `assertContainsSubsequence`

assertContainsSubsequence(
        container, subsequence, msg=None
    )

Asserts that "container" contains "subsequence" as a subsequence.

Asserts that "container" contains all the elements of "subsequence", in order, but possibly with other elements interspersed. For example, \[1, 2, 3\] is a subsequence of \[0, 0, 1, 2, 0, 3, 0\] but not of \[0, 0, 1, 3, 0, 2, 0\].

|     |     |
| --- | --- |
| Args |     |
| `container` | the list we're testing for subsequence inclusion. |
| `subsequence` | the list we hope will be a subsequence of container. |
| `msg` | Optional message to report on failure. |

### `assertContainsSubset`

assertContainsSubset(
        expected_subset, actual_set, msg=None
    )

Checks whether actual iterable is a superset of expected iterable.

### `assertCountEqual`

assertCountEqual(
        first, second, msg=None
    )

Asserts that two iterables have the same elements, the same number of times, without regard to order.

self.assertEqual(Counter(list(first)),
                     Counter(list(second)))

Example:

- [0, 1, 1] and [1, 0, 1] compare equal.
    - [0, 0, 1] and [0, 1] compare unequal.

### `assertDTypeEqual`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L3701-L3714)

assertDTypeEqual(
        target, expected_dtype
    )

Assert ndarray data type is equal to expected.

|     |     |
| --- | --- |
| Args |     |
| `target` | The numpy `ndarray`, or anything that can be converted into a numpy `ndarray` (including Tensor). |
| `expected_dtype` | Expected data type. |

### `assertDataclassEqual`

assertDataclassEqual(
        first, second, msg=None
    )

Asserts two dataclasses are equal with more informative errors.

Arguments must both be dataclasses. This compares equality of individual fields and takes care to not compare fields that are marked as non-comparable. It gives per field differences, which are easier to parse than the comparison of the string representations from assertEqual.

In cases where the dataclass has a custom **eq**, and it is defined in a way that is inconsistent with equality of comparable fields, we raise an exception without further trying to figure out how they are different.

|     |     |
| --- | --- |
| Args |     |
| `first` | A dataclass, the first value. |
| `second` | A dataclass, the second value. |
| `msg` | An optional str, the associated message. |

|     |     |
| --- | --- |
| Raises |     |
| `AssertionError` | if the dataclasses are not equal. |

### `assertDeviceEqual`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L3803-L3815)

assertDeviceEqual(
        device1, device2, msg=None
    )

Asserts that the two given devices are the same.

|     |     |
| --- | --- |
| Args |     |
| `device1` | A string device name or TensorFlow `DeviceSpec` object. |
| `device2` | A string device name or TensorFlow `DeviceSpec` object. |
| `msg` | Optional message to report on failure. |

### `assertDictAlmostEqual`

assertDictAlmostEqual(
        a, b, places=None, msg=None, delta=None
    )

Raises AssertionError if a and b are not equal or almost equal dicts.

This is like assertDictEqual, except for float values which are compared using assertAlmostEqual. Almost equality is determined for float values by:

*   have numeric difference less than the given delta, or
*   equal if rounded to the given number of decimal places after the decimal point (default 7).

|     |     |
| --- | --- |
| Args |     |
| `a` | A dict, the expected value. |
| `b` | A dict, the actual value. |
| `places` | The number of decimal places to compare for floats. |
| `msg` | An optional str, the associated message. |
| `delta` | The OK difference between compared values for floats. |

|     |     |
| --- | --- |
| Raises |     |
| `AssertionError` | if the dictionaries are not equal or almost equal. |
| `ValueError` | if both places and delta are specified. |

### `assertDictContainsSubset`

assertDictContainsSubset(
        subset: abc.Mapping[Any, Any], dictionary: abc.Mapping[Any, Any], msg=None
    )

Raises AssertionError if "dictionary" is not a superset of "subset".

|     |     |
| --- | --- |
| Args |     |
| `subset` | A dict, the expected subset of the "dictionary". |
| `dictionary` | A dict, the actual value. |
| `msg` | An optional str, the associated message. |

|     |     |
| --- | --- |
| Raises |     |
| `AssertionError` | if "dictionary" is not a superset of "subset". |

### `assertDictEqual`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L3817-L3841)

assertDictEqual(
        a, b, msg=None
    )

Assert that two given dictionary of tensors are the same.

|     |     |
| --- | --- |
| Args |     |
| `a` | Expected dictionary with numpy ndarray or anything else that can be converted to one as values. |
| `b` | Actual dictionary with numpy ndarray or anything else that can be converted to one as values. |
| `msg` | Optional message to report on failure. |

### `assertEmpty`

assertEmpty(
        container, msg=None
    )

Asserts that an object has zero length.

|     |     |
| --- | --- |
| Args |     |
| `container` | Anything that implements the collections.abc.Sized interface. |
| `msg` | Optional message to report on failure. |

### `assertEndsWith`

assertEndsWith(
        actual, expected_end, msg=None
    )

Asserts that actual.endswith(expected\_end) is True.

|     |     |
| --- | --- |
| Args |     |
| `actual` | str |
| `expected_end` | str |
| `msg` | Optional message to report on failure. |

### `assertEqual`

assertEqual(
        first, second, msg=None
    )

Fail if the two objects are unequal as determined by the '==' operator.

### `assertEquals`

assertEquals(
        *args, **kwargs
    )

### `assertFalse`

assertFalse(
        expr, msg=None
    )

Check that the expression is false.

### `assertGreater`

assertGreater(
        a, b, msg=None
    )

Just like self.assertTrue(a > b), but with a nicer default message.

### `assertGreaterEqual`

assertGreaterEqual(
        a, b, msg=None
    )

Just like self.assertTrue(a >= b), but with a nicer default message.

### `assertIn`

assertIn(
        member, container, msg=None
    )

Just like self.assertTrue(a in b), but with a nicer default message.

### `assertIs`

assertIs(
        expr1, expr2, msg=None
    )

Just like self.assertTrue(a is b), but with a nicer default message.

### `assertIsInstance`

assertIsInstance(
        obj, cls, msg=None
    )

Same as self.assertTrue(isinstance(obj, cls)), with a nicer default message.

### `assertIsNone`

assertIsNone(
        obj, msg=None
    )

Same as self.assertTrue(obj is None), with a nicer default message.

### `assertIsNot`

assertIsNot(
        expr1, expr2, msg=None
    )

Just like self.assertTrue(a is not b), but with a nicer default message.

### `assertIsNotNone`

assertIsNotNone(
        obj, msg=None
    )

Included for symmetry with assertIsNone.

### `assertIsSubclass`

assertIsSubclass(
        cls, superclass, msg=None
    )

Asserts that issubclass(cls, superclass) is True.

Copied from unittest.TestCase.assertIsSubclass, added in Python 3.14.

|     |     |
| --- | --- |
| Args |     |
| `cls` | The class to check. |
| `superclass` | A class, or a tuple of classes, as accepted by issubclass(). |
| `msg` | Optional message to report on failure. |

### `assertItemsEqual`

assertItemsEqual(
        first, second, msg=None
    )

Asserts that two iterables have the same elements, the same number of times, without regard to order.

self.assertEqual(Counter(list(first)),
                     Counter(list(second)))

Example:

- [0, 1, 1] and [1, 0, 1] compare equal.
    - [0, 0, 1] and [0, 1] compare unequal.

### `assertJsonEqual`

assertJsonEqual(
        first, second, msg=None
    )

Asserts that the JSON objects defined in two strings are equal.

A summary of the differences will be included in the failure message using assertSameStructure.

|     |     |
| --- | --- |
| Args |     |
| `first` | A string containing JSON to decode and compare to second. |
| `second` | A string containing JSON to decode and compare to first. |
| `msg` | Additional text to include in the failure message. |

### `assertLen`

assertLen(
        container, expected_len, msg=None
    )

Asserts that an object has the expected length.

|     |     |
| --- | --- |
| Args |     |
| `container` | Anything that implements the collections.abc.Sized interface. |
| `expected_len` | The expected length of the container. |
| `msg` | Optional message to report on failure. |

### `assertLess`

assertLess(
        a, b, msg=None
    )

Just like self.assertTrue(a < b), but with a nicer default message.

### `assertLessEqual`

assertLessEqual(
        a, b, msg=None
    )

Just like self.assertTrue(a <= b), but with a nicer default message.

### `assertListEqual`

assertListEqual(
        list1, list2, msg=None
    )

A list-specific equality assertion.

|     |     |
| --- | --- |
| Args |     |
| `list1` | The first list to compare. |
| `list2` | The second list to compare. |
| `msg` | Optional message to use on failure instead of a list of differences. |

### `assertLogs`

assertLogs(
        logger=None, level=None
    )

Fail unless a log message of level _level_ or higher is emitted on _logger\_name_ or its children. If omitted, _level_ defaults to INFO and _logger_ defaults to the root logger.

This method must be used as a context manager, and will yield a recording object with two attributes: `output` and `records`. At the end of the context manager, the `output` attribute will be a list of the matching formatted log messages and the `records` attribute will be a list of the corresponding LogRecord objects.

Example::

with self.assertLogs('foo', level='INFO') as cm:
        logging.getLogger('foo').info('first message')
        logging.getLogger('foo.bar').error('second message')
    self.assertEqual(cm.output, ['INFO:foo:first message',\
                                 'ERROR:foo.bar:second message'])

### `assertMappingEqual`

assertMappingEqual(
        a,
        b,
        msg=None,
        mapping_type=abc.Mapping,
        check_values_equality=(lambda x, y: (x == y, None))
    )

Raises AssertionError if a and b differ in keys or values.

Key sets must be exectly the same, the corresponding values should satisfy the provided equality function.

|     |     |
| --- | --- |
| Args |     |
| `a` | A mapping, the expected value. |
| `b` | A mapping, the actual value. |
| `msg` | An optional str, the associated message. |
| `mapping_type` | The expected type of the mappings. |
| `check_values_equality` | A function that takes two values and returns a tuple of (bool, BaseException), where the bool is True if the values are equal and the BaseException is an optional exception occured during the equality check. |

|     |     |
| --- | --- |
| Raises |     |
| `AssertionError` | if the dictionaries are not equal. |

### `assertMultiLineEqual`

assertMultiLineEqual(
        first, second, msg=None, **kwargs
    )

Asserts that two multi-line strings are equal.

### `assertNDArrayNear`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L3175-L3185)

assertNDArrayNear(
        ndarray1, ndarray2, err, msg=None
    )

Asserts that two numpy arrays have near values.

|     |     |
| --- | --- |
| Args |     |
| `ndarray1` | a numpy ndarray. |
| `ndarray2` | a numpy ndarray. |
| `err` | a float. The maximum absolute difference allowed. |
| `msg` | Optional message to report on failure. |

### `assertNear`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L3131-L3153)

assertNear(
        f1, f2, err, msg=None
    )

Asserts that two floats are near each other.

Checks that |f1 - f2| < err and asserts a test failure if not.

|     |     |
| --- | --- |
| Args |     |
| `f1` | A float value. |
| `f2` | A float value. |
| `err` | A float value. |
| `msg` | An optional string message to append to the failure message. |

### `assertNoCommonElements`

assertNoCommonElements(
        expected_seq, actual_seq, msg=None
    )

Checks whether actual iterable and expected iterable are disjoint.

### `assertNoLogs`

assertNoLogs(
        logger=None, level=None
    )

Fail unless no log messages of level _level_ or higher are emitted on _logger\_name_ or its children.

This method must be used as a context manager.

### `assertNotAllClose`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L3434-L3457)

assertNotAllClose(
        a, b, rtol=1e-06, atol=1e-06, msg=None
    )

Assert that two numpy arrays, or Tensors, do not have near values.

|     |     |
| --- | --- |
| Args |     |
| `a` | The expected numpy `ndarray`, or anything that can be converted into a numpy `ndarray` (including Tensor), or any arbitrarily nested of structure of these. |
| `b` | The actual numpy `ndarray`, or anything that can be converted into a numpy `ndarray` (including Tensor), or any arbitrarily nested of structure of these. |
| `rtol` | relative tolerance. |
| `atol` | absolute tolerance. |
| `msg` | Optional message to report on failure. |

|     |     |
| --- | --- |
| Raises |     |
| `AssertionError` | If `a` and `b` are unexpectedly close at all elements. |

### `assertNotAllEqual`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L3519-L3533)

assertNotAllEqual(
        a, b, msg=None
    )

Asserts that two numpy arrays or Tensors do not have the same values.

|     |     |
| --- | --- |
| Args |     |
| `a` | the expected numpy ndarray or anything can be converted to one. |
| `b` | the actual numpy ndarray or anything can be converted to one. |
| `msg` | Optional message to report on failure. |

### `assertNotAlmostEqual`

assertNotAlmostEqual(
        first, second, places=None, msg=None, delta=None
    )

Fail if the two objects are equal as determined by their difference rounded to the given number of decimal places (default 7) and comparing to zero, or by comparing that the difference between the two objects is less than the given delta.

Note that decimal places (from zero) are usually not the same as significant digits (measured from the most significant digit).

Objects that are equal automatically fail.

### `assertNotAlmostEquals`

assertNotAlmostEquals(
        *args, **kwargs
    )

### `assertNotEmpty`

assertNotEmpty(
        container, msg=None
    )

Asserts that an object has non-zero length.

|     |     |
| --- | --- |
| Args |     |
| `container` | Anything that implements the collections.abc.Sized interface. |
| `msg` | Optional message to report on failure. |

### `assertNotEndsWith`

assertNotEndsWith(
        actual, unexpected_end, msg=None
    )

Asserts that actual.endswith(unexpected\_end) is False.

|     |     |
| --- | --- |
| Args |     |
| `actual` | str |
| `unexpected_end` | str |
| `msg` | Optional message to report on failure. |

### `assertNotEqual`

assertNotEqual(
        first, second, msg=None
    )

Fail if the two objects are equal as determined by the '!=' operator.

### `assertNotEquals`

assertNotEquals(
        *args, **kwargs
    )

### `assertNotIn`

assertNotIn(
        member, container, msg=None
    )

Just like self.assertTrue(a not in b), but with a nicer default message.

### `assertNotIsInstance`

assertNotIsInstance(
        obj, cls, msg=None
    )

Included for symmetry with assertIsInstance.

### `assertNotIsSubclass`

assertNotIsSubclass(
        cls, superclass, msg=None
    )

Asserts that issubclass(cls, superclass) is False.

Copied from unittest.TestCase.assertNotIsSubclass, added in Python 3.14.

|     |     |
| --- | --- |
| Args |     |
| `cls` | The class to check. |
| `superclass` | A class, or a tuple of classes, as accepted by issubclass(). |
| `msg` | Optional message to report on failure. |

### `assertNotRegex`

assertNotRegex(
        text, unexpected_regex, msg=None
    )

Fail the test if the text matches the regular expression.

### `assertNotRegexpMatches`

assertNotRegexpMatches(
        *args, **kwargs
    )

### `assertNotStartsWith`

assertNotStartsWith(
        actual, unexpected_start, msg=None
    )

Asserts that actual.startswith(unexpected\_start) is False.

|     |     |
| --- | --- |
| Args |     |
| `actual` | str |
| `unexpected_start` | str |
| `msg` | Optional message to report on failure. |

### `assertProtoEquals`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L2737-L2782)

assertProtoEquals(
        expected_message_maybe_ascii,
        validate_message,
        msg=None,
        relative_tolerance=None
    )

Asserts that message is same as parsed expected\_message\_ascii.

Creates another prototype of message, reads the ascii message into it and then compares them using self.\_AssertProtoEqual().

|     |     |
| --- | --- |
| Args |     |
| `expected_message_maybe_ascii` | proto message in original or ascii form. |
| `validate_message` | the message to validate. |
| `msg` | Optional message to report on failure. |
| `relative_tolerance` | float. The allowable difference between the two values being compared is determined by multiplying the relative tolerance by the maximum of the two values. If this is not provided, then all floats are compared using string comparison. |

### `assertProtoEqualsVersion`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L2784-L2793)

assertProtoEqualsVersion(
        expected,
        actual,
        producer=versions.GRAPH_DEF_VERSION,
        min_consumer=versions.GRAPH_DEF_VERSION_MIN_CONSUMER,
        msg=None
    )

### `assertRaises`

assertRaises(
        expected_exception, *args, **kwargs
    )

Fail unless an exception of class expected\_exception is raised by the callable when invoked with specified positional and keyword arguments. If a different type of exception is raised, it will not be caught, and the test case will be deemed to have suffered an error, exactly as for an unexpected exception.

If called with the callable and arguments omitted, will return a context object used like this::

 with self.assertRaises(SomeException):
         do_something()

An optional keyword argument 'msg' can be provided when assertRaises is used as a context object.

The context manager keeps a reference to the exception as the 'exception' attribute. This allows you to inspect the exception after the assertion::

with self.assertRaises(SomeException) as cm:
        do_something()
    the_exception = cm.exception
    self.assertEqual(the_exception.error_code, 3)

### `assertRaisesIncompatibleShapesError`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L3769-L3773)

assertRaisesIncompatibleShapesError(
        exception_type=tf.errors.InvalidArgumentError
    )

### `assertRaisesOpError`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L3765-L3767)

assertRaisesOpError(
        expected_err_re_or_predicate
    )

### `assertRaisesRegex`

assertRaisesRegex(
        expected_exception, expected_regex, *args, **kwargs
    )

Asserts that the message in a raised exception matches a regex.

|     |     |
| --- | --- |
| Args |     |
| `expected_exception` | Exception class expected to be raised. |
| `expected_regex` | Regex (re.Pattern object or string) expected to be found in error message. |
| `args` | Function to be called and extra positional args. |
| `kwargs` | Extra kwargs. |
| `msg` | Optional message used in case of failure. Can only be used when assertRaisesRegex is used as a context manager. |

### `assertRaisesRegexp`

assertRaisesRegexp(
        expected_exception, expected_regex, *args, **kwargs
    )

Asserts that the message in a raised exception matches a regex.

|     |     |
| --- | --- |
| Args |     |
| `expected_exception` | Exception class expected to be raised. |
| `expected_regex` | Regex (re.Pattern object or string) expected to be found in error message. |
| `args` | Function to be called and extra positional args. |
| `kwargs` | Extra kwargs. |
| `msg` | Optional message used in case of failure. Can only be used when assertRaisesRegex is used as a context manager. |

### `assertRaisesWithLiteralMatch`

assertRaisesWithLiteralMatch(
        expected_exception,
        expected_exception_message,
        callable_obj=None,
        *args,
        **kwargs
    )

Asserts that the message in a raised exception equals the given string.

Unlike assertRaisesRegex, this method takes a literal string, not a regular expression.

with self.assertRaisesWithLiteralMatch(ExType, 'message'): DoSomething()

|     |     |
| --- | --- |
| Args |     |
| `expected_exception` | Exception class expected to be raised. |
| `expected_exception_message` | String message expected in the raised exception. For a raise exception e, expected\_exception\_message must equal str(e). |
| `callable_obj` | Function to be called, or None to return a context. |
| `*args` | Extra args. |
| `**kwargs` | Extra kwargs. |

|     |
| --- |
| Returns |     |
| A context manager if callable\_obj is None. Otherwise, None. |     |

|     |
| --- |
| Raises |     |
| self.failureException if callable\_obj does not raise a matching exception. |     |

### `assertRaisesWithPredicateMatch`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L3717-L3761)

@contextlib.contextmanager

Returns a context manager to enclose code expected to raise an exception.

If the exception is an OpError, the op stack is also included in the message predicate search.

|     |     |
| --- | --- |
| Args |     |
| `exception_type` | The expected type of exception that should be raised. |
| `expected_err_re_or_predicate` | If this is callable, it should be a function of one argument that inspects the passed-in exception and returns True (success) or False (please fail the test). Otherwise, the error message is expected to match this regular expression partially. |

|     |
| --- |
| Returns |     |
| A context manager to surround code that is expected to raise an exception. |     |

### `assertRegex`

assertRegex(
        text, expected_regex, msg=None
    )

Fail the test unless the text matches the regular expression.

### `assertRegexMatch`

assertRegexMatch(
        actual_str, regexes, message=None
    )

Asserts that at least one regex in regexes matches str.

If possible you should use `assertRegex`, which is a simpler version of this method. `assertRegex` takes a single regular expression (a string or re compiled object) instead of a list.

#### Notes:

1.  This function uses substring matching, i.e. the matching succeeds if _any_ substring of the error message matches _any_ regex in the list. This is more convenient for the user than full-string matching.
    
2.  If regexes is the empty list, the matching will always fail.
    
3.  Use regexes=\[''\] for a regex that will always pass.
    
4.  '.' matches any single character _except_ the newline. To match any character, use '(.|\\n)'.
    
5.  '^' matches the beginning of each line, not just the beginning of the string. Similarly, '$' matches the end of each line.
    
6.  An exception will be thrown if regexes contains an invalid regex.
    

|     |     |
| --- | --- |
| Args |     |
| `actual_str` | The string we try to match with the items in regexes. |
| `regexes` | The regular expressions we want to match against str. See "Notes" above for detailed notes on how this is interpreted. |
| `message` | The message to be printed if the test fails. |

### `assertRegexpMatches`

assertRegexpMatches(
        *args, **kwargs
    )

### `assertSameElements`

assertSameElements(
        expected_seq, actual_seq, msg=None
    )

Asserts that two sequences have the same elements (in any order).

This method, unlike assertCountEqual, doesn't care about any duplicates in the expected and actual sequences::

# Doesn't raise an AssertionError
    assertSameElements([1, 1, 1, 0, 0, 0], [0, 1])

If possible, you should use assertCountEqual instead of assertSameElements.

|     |     |
| --- | --- |
| Args |     |
| `expected_seq` | A sequence containing elements we are expecting. |
| `actual_seq` | The sequence that we are testing. |
| `msg` | The message to be printed if the test fails. |

### `assertSameStructure`

assertSameStructure(
        a, b, aname='a', bname='b', msg=None
    )

Asserts that two values contain the same structural content.

The two arguments should be data trees consisting of trees of dicts and lists. They will be deeply compared by walking into the contents of dicts and lists; other items will be compared using the == operator. If the two structures differ in content, the failure message will indicate the location within the structures where the first difference is found. This may be helpful when comparing large structures.

Mixed Sequence and Set types are supported. Mixed Mapping types are supported, but the order of the keys will not be considered in the comparison.

|     |     |
| --- | --- |
| Args |     |
| `a` | The first structure to compare. |
| `b` | The second structure to compare. |
| `aname` | Variable name to use for the first structure in assertion messages. |
| `bname` | Variable name to use for the second structure. |
| `msg` | Additional text to include in the failure message. |

### `assertSequenceAlmostEqual`

assertSequenceAlmostEqual(
        expected_seq, actual_seq, places=None, msg=None, delta=None
    )

An approximate equality assertion for ordered sequences.

Fail if the two sequences are unequal as determined by their value differences rounded to the given number of decimal places (default 7) and comparing to zero, or by comparing that the difference between each value in the two sequences is more than the given delta.

Note that decimal places (from zero) are usually not the same as significant digits (measured from the most significant digit).

If the two sequences compare equal then they will automatically compare almost equal.

|     |     |
| --- | --- |
| Args |     |
| `expected_seq` | A sequence containing elements we are expecting. |
| `actual_seq` | The sequence that we are testing. |
| `places` | The number of decimal places to compare. |
| `msg` | The message to be printed if the test fails. |
| `delta` | The OK difference between compared values. |

### `assertSequenceEqual`

assertSequenceEqual(
        seq1, seq2, msg=None, seq_type=None
    )

An equality assertion for ordered sequences (like lists and tuples).

For the purposes of this function, a valid ordered sequence type is one which can be indexed, has a length, and has an equality operator.

|     |     |
| --- | --- |
| Args |     |
| `seq1` | The first sequence to compare. |
| `seq2` | The second sequence to compare. |
| `seq_type` | The expected datatype of the sequences, or None if no datatype should be enforced. |
| `msg` | Optional message to use on failure instead of a list of differences. |

### `assertSequenceStartsWith`

assertSequenceStartsWith(
        prefix, whole, msg=None
    )

An equality assertion for the beginning of ordered sequences.

If prefix is an empty sequence, it will raise an error unless whole is also an empty sequence.

If prefix is not a sequence, it will raise an error if the first element of whole does not match.

|     |     |
| --- | --- |
| Args |     |
| `prefix` | A sequence expected at the beginning of the whole parameter. |
| `whole` | The sequence in which to look for prefix. |
| `msg` | Optional message to report on failure. |

### `assertSetEqual`

assertSetEqual(
        set1, set2, msg=None
    )

A set-specific equality assertion.

|     |     |
| --- | --- |
| Args |     |
| `set1` | The first set to compare. |
| `set2` | The second set to compare. |
| `msg` | Optional message to use on failure instead of a list of differences. |

assertSetEqual uses ducktyping to support different types of sets, and is optimized for sets specifically (parameters must support a difference method).

### `assertShapeEqual`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L3775-L3801)

assertShapeEqual(
        input_a, input_b, msg=None
    )

Asserts that two Numpy or TensorFlow objects have the same shape.

For Tensors, this compares statically known shapes at compile time, not dynamic shapes at runtime.

|     |     |
| --- | --- |
| Args |     |
| `input_a` | A Numpy ndarray, Numpy scalar, or a Tensor. |
| `input_b` | A Numpy ndarray, Numpy scalar, or a Tensor. |
| `msg` | Optional message to report on failure. |

|     |     |
| --- | --- |
| Raises |     |
| `TypeError` | If the arguments have the wrong type. |

### `assertStartsWith`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L2795-L2806)

assertStartsWith(
        actual, expected_start, msg=None
    )

Assert that actual.startswith(expected\_start) is True.

|     |     |
| --- | --- |
| Args |     |
| `actual` | str |
| `expected_start` | str |
| `msg` | Optional message to report on failure. |

### `assertTotallyOrdered`

assertTotallyOrdered(
        *groups, **kwargs
    )

Asserts that total ordering has been implemented correctly.

For example, say you have a class A that compares only on its attribute x. Comparators other than `__lt__` are omitted for brevity::

class A(object):
      def __init__(self, x, y):
        self.x = x
        self.y = y
    
      def __hash__(self):
        return hash(self.x)
    
      def __lt__(self, other):
        try:
          return self.x < other.x
        except AttributeError:
          return NotImplemented

assertTotallyOrdered will check that instances can be ordered correctly. For example::

self.assertTotallyOrdered(
        [None],  # None should come before everything else.
        [1],  # Integers sort earlier.
        [A(1, 'a')],
        [A(2, 'b')],  # 2 is after 1.
        [A(3, 'c'), A(3, 'd')],  # The second argument is irrelevant.
        [A(4, 'z')],
        ['foo'])  # Strings sort last.

|     |     |
| --- | --- |
| Args |     |
| `*groups` | A list of groups of elements. Each group of elements is a list of objects that are equal. The elements in each group must be less than the elements in the group after it. For example, these groups are totally ordered: `[None]`, `[1]`, `[2, 2]`, `[3]`. |
| `**kwargs` | optional msg keyword argument can be passed. |

### `assertTrue`

assertTrue(
        expr, msg=None
    )

Check that the expression is true.

### `assertTupleEqual`

assertTupleEqual(
        tuple1, tuple2, msg=None
    )

A tuple-specific equality assertion.

|     |     |
| --- | --- |
| Args |     |
| `tuple1` | The first tuple to compare. |
| `tuple2` | The second tuple to compare. |
| `msg` | Optional message to use on failure instead of a list of differences. |

### `assertUrlEqual`

assertUrlEqual(
        a, b, msg=None
    )

Asserts that urls are equal, ignoring ordering of query params.

### `assertWarns`

assertWarns(
        expected_warning, *args, **kwargs
    )

Fail unless a warning of class warnClass is triggered by the callable when invoked with specified positional and keyword arguments. If a different type of warning is triggered, it will not be handled: depending on the other warning filtering rules in effect, it might be silenced, printed out, or raised as an exception.

If called with the callable and arguments omitted, will return a context object used like this::

 with self.assertWarns(SomeWarning):
         do_something()

An optional keyword argument 'msg' can be provided when assertWarns is used as a context object.

The context manager keeps a reference to the first matching warning as the 'warning' attribute; similarly, the 'filename' and 'lineno' attributes give you information about the line of Python code from which the warning was triggered. This allows you to inspect the warning after the assertion::

with self.assertWarns(SomeWarning) as cm:
        do_something()
    the_warning = cm.warning
    self.assertEqual(the_warning.some_attribute, 147)

### `assertWarnsRegex`

assertWarnsRegex(
        expected_warning, expected_regex, *args, **kwargs
    )

Asserts that the message in a triggered warning matches a regexp. Basic functioning is similar to assertWarns() with the addition that only warnings whose messages also match the regular expression are considered successful matches.

|     |     |
| --- | --- |
| Args |     |
| `expected_warning` | Warning class expected to be triggered. |
| `expected_regex` | Regex (re.Pattern object or string) expected to be found in error message. |
| `args` | Function to be called and extra positional args. |
| `kwargs` | Extra kwargs. |
| `msg` | Optional message used in case of failure. Can only be used when assertWarnsRegex is used as a context manager. |

### `assert_`

assert_(
        *args, **kwargs
    )

### `cached_session`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L2927-L2979)

@contextlib.contextmanager

Returns a TensorFlow Session for use in executing tests.

This method behaves differently than self.session(): for performance reasons `cached_session` will by default reuse the same session within the same test. The session returned by this function will only be closed at the end of the test (in the TearDown function).

Use the `use_gpu` and `force_gpu` options to control where ops are run. If `force_gpu` is True, all ops are pinned to `/device:GPU:0`. Otherwise, if `use_gpu` is True, TensorFlow tries to run as many ops on the GPU as possible. If both `force_gpu and`use\_gpu\` are False, all ops are pinned to the CPU.

#### Example:

class MyOperatorTest(test_util.TensorFlowTestCase):
      def testMyOperator(self):
        with self.cached_session() as sess:
          valid_input = [1.0, 2.0, 3.0, 4.0, 5.0]
          result = MyOperator(valid_input).eval()
          self.assertEqual(result, [1.0, 2.0, 3.0, 5.0, 8.0]
          invalid_input = [-1.0, 2.0, 7.0]
          with self.assertRaisesOpError("negative input not supported"):
            MyOperator(invalid_input).eval()

|     |     |
| --- | --- |
| Args |     |
| `graph` | Optional graph to use during the returned session. |
| `config` | An optional config\_pb2.ConfigProto to use to configure the session. |
| `use_gpu` | If True, attempt to run as many ops as possible on GPU. |
| `force_gpu` | If True, pin all ops to `/device:GPU:0`. |

|     |
| --- |
| Yields |     |
| A Session object that should be used as a context manager to surround the graph building and execution code in a test case. |     |

### `captureWritesToStream`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L2666-L2709)

@contextlib.contextmanager

A context manager that captures the writes to a given stream.

This context manager captures all writes to a given stream inside of a `CapturedWrites` object. When this context manager is created, it yields the `CapturedWrites` object. The captured contents can be accessed by calling `.contents()` on the `CapturedWrites`.

For this function to work, the stream must have a file descriptor that can be modified using `os.dup` and `os.dup2`, and the stream must support a `.flush()` method. The default python sys.stdout and sys.stderr are examples of this. Note that this does not work in Colab or Jupyter notebooks, because those use alternate stdout streams.

#### Example:

class MyOperatorTest(test_util.TensorFlowTestCase):
      def testMyOperator(self):
        input = [1.0, 2.0, 3.0, 4.0, 5.0]
        with self.captureWritesToStream(sys.stdout) as captured:
          result = MyOperator(input).eval()
        self.assertStartsWith(captured.contents(), "This was printed.")

|     |     |
| --- | --- |
| Args |     |
| `stream` | The stream whose writes should be captured. This stream must have a file descriptor, support writing via using that file descriptor, and must have a `.flush()` method. |

|     |
| --- |
| Yields |     |
| A `CapturedWrites` object that contains all writes to the specified stream made during this context. |     |

### `checkedThread`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L3105-L3128)

checkedThread(
        target: Callable[..., Any],
        args: Optional[tuple[Any, ...]] = None,
        kwargs: Optional[dict[str, Any]] = None
    ) -> _CheckedThread

Returns a Thread wrapper that asserts 'target' completes successfully.

This method should be used to create all threads in test cases, as otherwise there is a risk that a thread will silently fail, and/or assertions made in the thread will not be respected.

|     |     |
| --- | --- |
| Args |     |
| `target` | A callable object to be executed in the thread. |
| `args` | The argument tuple for the target invocation. Defaults to (). |
| `kwargs` | A dictionary of keyword arguments for the target invocation. Defaults to {}. |

|     |
| --- |
| Returns |     |
| A wrapper for threading.Thread that supports start() and join() methods. |     |

### `countTestCases`

countTestCases()

### `create_tempdir`

create_tempdir(
        name: (str | None) = None, cleanup: (TempFileCleanup | None) = None
    ) -> _TempDir

Create a temporary directory specific to the test.

This creates a named directory on disk that is isolated to this test, and will be properly cleaned up by the test. This avoids several pitfalls of creating temporary directories for test purposes, as well as makes it easier to setup directories and verify their contents. For example::

def test_foo(self):
      out_dir = self.create_tempdir()
      out_log = out_dir.create_file('output.log')
      expected_outputs = [\
          os.path.join(out_dir, 'data-0.txt'),\
          os.path.join(out_dir, 'data-1.txt'),\
      ]
      code_under_test(out_dir)
      self.assertTrue(os.path.exists(expected_paths[0]))
      self.assertTrue(os.path.exists(expected_paths[1]))
      self.assertEqual('foo', out_log.read_text())

See also: :meth:`create_tempfile` for creating temporary files.

|     |     |
| --- | --- |
| Args |     |
| `name` | Optional name of the directory. If not given, a unique name will be generated and used. |
| `cleanup` | Optional cleanup policy on when/if to remove the directory (and all its contents) at the end of the test. If None, then uses :attr:`tempfile_cleanup`. |

|     |
| --- |
| Returns |     |
| A \_TempDir representing the created directory; see \_TempDir class docs for usage. |     |

### `create_tempfile`

create_tempfile(
        file_path: (str | None) = None,
        content: (AnyStr | None) = None,
        mode: str = 'w',
        encoding: str = 'utf8',
        errors: str = 'strict',
        cleanup: (TempFileCleanup | None) = None
    ) -> _TempFile

Create a temporary file specific to the test.

This creates a named file on disk that is isolated to this test, and will be properly cleaned up by the test. This avoids several pitfalls of creating temporary files for test purposes, as well as makes it easier to setup files, their data, read them back, and inspect them when a test fails. For example::

def test_foo(self):
      output = self.create_tempfile()
      code_under_test(output)
      self.assertGreater(os.path.getsize(output), 0)
      self.assertEqual('foo', output.read_text())

See also: :meth:`create_tempdir` for creating temporary directories, and `_TempDir.create_file` for creating files within a temporary directory.

|     |     |
| --- | --- |
| Args |     |
| `file_path` | Optional file path for the temp file. If not given, a unique file name will be generated and used. Slashes are allowed in the name; any missing intermediate directories will be created. NOTE: This path is the path that will be cleaned up, including any directories in the path, e.g., `'foo/bar/baz.txt'` will `rm -r foo`. |
| `content` | Optional string or bytes to initially write to the file. If not specified, then an empty file is created. |
| `mode` | Mode string to use when writing content. Only used if `content` is non-empty. |
| `encoding` | Encoding to use when writing string content. Only used if `content` is text. |
| `errors` | How to handle text to bytes encoding errors. Only used if `content` is text. |
| `cleanup` | Optional cleanup policy on when/if to remove the directory (and all its contents) at the end of the test. If None, then uses :attr:`tempfile_cleanup`. |

|     |
| --- |
| Returns |     |
| A \_TempFile representing the created file; see \_TempFile class docs for usage. |     |

### `debug`

debug()

Run the test without collecting errors in a TestResult

### `defaultTestResult`

defaultTestResult()

### `doClassCleanups`

@classmethod

Execute all class cleanup functions. Normally called for you after tearDownClass.

### `doCleanups`

doCleanups()

Execute all cleanup functions. Normally called for you after tearDown.

### `enterClassContext`

@classmethod

Same as enterContext, but class-wide.

### `enterContext`

enterContext(
        cm
    )

Enters the supplied context manager.

If successful, also adds its **exit** method as a cleanup function and returns the result of the **enter** method.

### `enter_context`

@classmethod

A classmethod version of enter\_context.

### `evaluate`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L2848-L2873)

evaluate(
        tensors
    ) -> Union[ragged_tensor_value.RaggedTensorValue, sparse_tensor.\
        SparseTensorValue, None]

Evaluates tensors and returns numpy values.

|     |     |
| --- | --- |
| Args |     |
| `tensors` | A Tensor or a nested list/tuple of Tensors. |

|     |
| --- |
| Returns |     |
| tensors numpy values. |     |

### `evaluate_if_both_tensors`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L3213-L3219)

evaluate_if_both_tensors(
        a, b
    )

### `fail`

fail(
        msg=None, user_msg=None
    ) -> NoReturn

Fail immediately with the given standard message and user message.

### `failIf`

failIf(
        *args, **kwargs
    )

### `failIfAlmostEqual`

failIfAlmostEqual(
        *args, **kwargs
    )

### `failIfEqual`

failIfEqual(
        *args, **kwargs
    )

### `failUnless`

failUnless(
        *args, **kwargs
    )

### `failUnlessAlmostEqual`

failUnlessAlmostEqual(
        *args, **kwargs
    )

### `failUnlessEqual`

failUnlessEqual(
        *args, **kwargs
    )

### `failUnlessRaises`

failUnlessRaises(
        *args, **kwargs
    )

### `get_recorded_properties`

get_recorded_properties(
        subtest=None
    ) -> dict[str, Any]

Returns any properties that the user has recorded.

If called from within a subtest and subtest is None, returns a dict made up of _both_ the subtest's properties _and_ the outer test's properties. (The subtest's properties take precedence in the event of a conflict.)

|     |     |
| --- | --- |
| Args |     |
| `subtest` | The subtest whose properties should be returned. Unlike the default case, if subtest is set, _only_ that subtest's properties are returned, not those of the enclosing test. |

### `get_temp_dir`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L2648-L2664)

get_temp_dir() -> str

Returns a unique temporary directory for the test to use.

If you call this method multiple times during in a test, it will return the same folder. However, across different runs the directories will be different. This will ensure that across different runs tests will not be able to pollute each others environment. If you need multiple unique directories within a single test, you should use tempfile.mkdtemp as follows: tempfile.mkdtemp(dir=self.get\_temp\_dir()):

|     |
| --- |
| Returns |     |
| string, the path to the unique temporary directory created for this test. |     |

### `id`

id()

### `record_property`

record_property(
        property_name: str, property_value: Any
    ) -> None

Record an arbitrary property for later use.

The property is attributed to the currently active subtest, if any, or the test itself, otherwise.

|     |     |
| --- | --- |
| Args |     |
| `property_name` | Name of property to record; must be a valid XML attribute name. |
| `property_value` | Value of property to record; must be a valid XML attribute value. |

### `run`

run(
        result=None
    )

### `session`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L2877-L2925)

@contextlib.contextmanager

A context manager for a TensorFlow Session for use in executing tests.

Note that this will set this session and the graph as global defaults.

Use the `use_gpu` and `force_gpu` options to control where ops are run. If `force_gpu` is True, all ops are pinned to `/device:GPU:0`. Otherwise, if `use_gpu` is True, TensorFlow tries to run as many ops on the GPU as possible. If both `force_gpu and`use\_gpu\` are False, all ops are pinned to the CPU.

#### Example:

class MyOperatorTest(test_util.TensorFlowTestCase):
      def testMyOperator(self):
        with self.session():
          valid_input = [1.0, 2.0, 3.0, 4.0, 5.0]
          result = MyOperator(valid_input).eval()
          self.assertEqual(result, [1.0, 2.0, 3.0, 5.0, 8.0]
          invalid_input = [-1.0, 2.0, 7.0]
          with self.assertRaisesOpError("negative input not supported"):
            MyOperator(invalid_input).eval()

|     |     |
| --- | --- |
| Args |     |
| `graph` | Optional graph to use during the returned session. |
| `config` | An optional config\_pb2.ConfigProto to use to configure the session. |
| `use_gpu` | If True, attempt to run as many ops as possible on GPU. |
| `force_gpu` | If True, pin all ops to `/device:GPU:0`. |

|     |
| --- |
| Yields |     |
| A Session object that should be used as a context manager to surround the graph building and execution code in a test case. |     |

### `setUp`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L2598-L2622)

setUp()

Hook method for setting up the test fixture before exercising it.

### `setUpClass`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L2624-L2628)

@classmethod

Hook method for setting up class fixture before running tests in the class.

### `shortDescription`

shortDescription() -> str

Formats both the test method name and the first line of its docstring.

If no docstring is given, only returns the method name.

This method overrides unittest.TestCase.shortDescription(), which only returns the first line of the docstring, obscuring the name of the test upon failure.

|     |     |
| --- | --- |
| Returns |     |
| `desc` | A short description of a test method. |

### `skipTest`

skipTest(
        reason
    )

Skip this test.

### `subTest`

@contextlib.contextmanager

Return a context manager that will return the enclosed block of code in a subtest identified by the optional message and keyword parameters. A failure in the subtest marks the test case as failed but resumes execution at the end of the enclosed block, allowing further test code to be executed.

### `tearDown`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L2630-L2641)

tearDown()

Hook method for deconstructing the test fixture after testing it.

### `tearDownClass`

@classmethod

Hook method for deconstructing the class fixture after running all tests in the class.

### `test_session`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L2981-L3009)

@contextlib.contextmanager

Use cached\_session instead. (deprecated)

### `__call__`

__call__(
        *args, **kwds
    )

Call self as a function.

### `__eq__`

__eq__(
        other
    )

Return self==value.

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| longMessage | `True` |
| maxDiff | `1600` |
| tempfile\_cleanup | `<TempFileCleanup.ALWAYS: 'always'>` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.